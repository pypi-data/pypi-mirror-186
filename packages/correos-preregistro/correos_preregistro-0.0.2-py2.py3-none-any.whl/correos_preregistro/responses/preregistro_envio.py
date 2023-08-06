from base64 import b64decode

from lxml import etree

from correos_preregistro.errors import ErrorDecodingPDFLabel, InvalidApiResponse


class ResponsePreregistroEnvio:
    shipment_code: str
    label_file: str

    def __init__(self, response):
        try:
            # TODO: Why???
            # shipment_code = root.xpath(".//CodEnvio")
            # label_file = root.xpath(".//Fichero")
            root = etree.fromstring(response)
            self.shipment_code = (
                root.getchildren()[1]
                .getchildren()[0]
                .getchildren()[-1]
                .getchildren()[1]
                .text
            )
            self.label_file = (
                root.getchildren()[1]
                .getchildren()[0]
                .getchildren()[-1]
                .getchildren()[-1]
                .getchildren()[-1]
                .getchildren()[-1]
                .text
            )
        except Exception:
            raise InvalidApiResponse(response)

    def get_pdf_label(self):
        try:
            return b64decode(self.label_file, validate=True)
        except Exception:
            raise ErrorDecodingPDFLabel("PDF label not valid")
