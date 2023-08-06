import requests

from .media import MediaType


class BotWhatsappPlugin:

    def __init__(self, access_token: str, whatsapp_number_id: str) -> None:
        """
        BotWhatsappPlugin

        Args:
            access_token (str): The account access token.
            whatsapp_number_id (str): The id referring to the Whatsapp number being used.
        """
        self.access_token = access_token
        self._url = f"https://graph.facebook.com/v13.0/{whatsapp_number_id}/messages"
        self._headers = {
            "Authorization": "Bearer {}".format(self.access_token),
            "Content-Type": "application/json"
        }

    def send_text_message(self, to_number: str, msg_content: str, preview_url=False) -> None:
        """
        Sends a text message via Whatsapp to the specified number.

        Args:
            to_number (str): The Whatsapp number that will receive the message.
            msg_content (str): The message body content.
            preview_url (boolean, optional): Include a preview box when a link is being sent in the message.
                Defaults to False.
        """
        message = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "text",
            "text": {"preview_url": preview_url, "body": msg_content}
        }
        self._post_message(message)

    def send_media_message(self, to_number: str, media_type: MediaType, media_link: str,
                           caption: str = None, filename: str = None) -> None:
        """
        Sends an message containing media via Whatsapp to the specified number.

        Args:
            to_number (str): The Whatsapp number that will receive the message.
            media_type (MediaType): The media type of the content that will be sent.
            media_link (str): The URL of the media content that will be sent in the message.
            caption (str, optional): The caption of an image or document that will be sent.
                (can be used only with image or document media type).
            filename(str, optional): The name of the document file that will be sent.
                (can be used only with document media type).
        """
        media_info = {"link": media_link}
        if caption:
            if media_type not in [MediaType.IMAGE, MediaType.DOCUMENT]:
                raise ValueError('The "caption" parameter can only be used with document or image media.')
            media_info.update({"caption": caption})

        if media_type != MediaType.DOCUMENT:
            if filename:
                raise ValueError('The "filename" parameter can only be used with document media.')
        else:
            filename = filename or "document"
            media_info.update({"filename": filename})

        message = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": media_type.value,
            media_type.value: media_info
        }
        self._post_message(message)

    def send_location_message(self, to_number: str, longitude: str, latitude: str, name: str,
                              address: str = None) -> None:
        """
        Sends an message containing a location via Whatsapp to the specified number.

        Args:
            to_number (str): The Whatsapp number that will receive the message.
            longitude (str): Longitude of the location.
            latitude (str): Latitude of the location.
            name (str): Name of the location.
            address (str, optional): Include location address in message.
        """
        message = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "location",
            "location": {
                "longitude": longitude,
                "latitude": latitude,
                "name": name,
                "address": address
            }
        }
        self._post_message(message)

    def send_contact_message(self, to_number: str, contact_name: str, contact_phone: str = None,
                             contact_email: str = None) -> None:
        """
        Sends an message containing a card with contact information via Whatsapp to the specified number.

        Args:
            to_number (str): The Whatsapp number that will receive the message.
            contact_name (str): Name of the contact.
            contact_phone (str, optional): Phone number of the contact.
            contact_email (str, optional): Email address of the contact.
        """
        message = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "contacts",
            "contacts": [{
                "name": {
                    "formatted_name": contact_name,
                    "first_name": contact_name
                },
                "phones": [{
                    "phone": contact_phone
                }],
                "emails": [{
                    "email": contact_email
                }]
            }]
        }
        self._post_message(message)

    def _post_message(self, message: dict):
        try:
            response = requests.post(self._url, headers=self._headers, json=message)
            response.raise_for_status()
        except requests.HTTPError as ex:
            raise ex
