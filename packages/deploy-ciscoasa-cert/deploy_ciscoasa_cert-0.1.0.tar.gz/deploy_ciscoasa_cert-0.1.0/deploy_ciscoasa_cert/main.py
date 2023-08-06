"""
deploy_ciscoasa_cert / main.py
Billy Zoellers, Dean Dorton

Deploy a .pfx certificate to a Cisco ASA
"""
import sys
import typer
from loguru import logger
from pathlib import Path
from datetime import datetime
import base64
from deploy_ciscoasa_cert.cisco_asa import CiscoASAREST

app = typer.Typer()


def date_string(prepend: str = "letsencrypt"):
    return f"{prepend}-{datetime.now().strftime('%Y%m%d')}"


def pkcs12_file_to_str(file_path: Path):
    """
    Take a PFX file and convert to string
    """
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        sys.exit(1)

    logger.info(f"Ingest and encode PFX")
    cert_pkcs12 = ["-----BEGIN PKCS12-----"]
    with open(file_path, "rb") as cert:
        encoded_string = base64.b64encode(cert.read())
        c = encoded_string
        while len(c) > 64:
            cert_pkcs12.append(c[:64].decode("utf-8"))
            c = c[64:]
        else:
            cert_pkcs12.append(c.decode("utf-8"))
    cert_pkcs12.append("-----END PKCS12-----")

    return cert_pkcs12


@app.command()
def main(
    pfx: Path = typer.Argument(..., help="Path to PFX file"),
    pfx_secret: str = typer.Option(..., help="PFX file secret"),
    hostname: str = typer.Option(..., help="Cisco ASA hostname"),
    username: str = typer.Option(..., help="Cisco ASA username"),
    password: str = typer.Option(..., help="Cisco ASA password"),
    verify_cert: bool = typer.Option(
        True, help="Verify the Cisco ASA REST API certificate"
    ),
    cert_name: str = typer.Option(date_string(), help="Name of certificate on ASA"),
):
    """
    Execution starts here
    """
    logger.info(f"Upload certificate to {hostname}")
    # Ingest .pfx file
    cert_pkcs12 = pkcs12_file_to_str(pfx)

    # Connect to ASA
    asa = CiscoASAREST(
        host=hostname, username=username, password=password, verify=verify_cert
    )

    # Upload certificate to ASA
    resp = asa.req(
        "certificate/identity",
        method="post",
        json={
            "certPass": pfx_secret,
            "kind": "object#IdentityCertificate",
            "certText": cert_pkcs12,
            "name": cert_name,
        },
    )
    logger.info(f"ASA response: {resp['messages'][0]['details']}")

    # Set new cert to active trustpoint
    cmd = f"ssl trust-point {cert_name} outside"
    resp = asa.req(
        "cli",
        method="post",
        json={
            "commands": [cmd, "write"],
        },
    )
    logger.info(f"ASA response: {resp['response'][1]}")
