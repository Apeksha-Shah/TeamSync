import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist

class CodeEditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extracting project_code from the URL path
        self.project_code = self.scope['url_route']['kwargs']['project_code']
        await self.accept()

    async def disconnect(self, close_code):
        # Handle disconnection
        pass

    async def receive(self, text_data):
        # Parsing incoming data from the WebSocket
        text_data_json = json.loads(text_data)
        html_code = text_data_json['html_code']
        css_code = text_data_json['css_code']
        js_code = text_data_json['js_code']

        # Save the received codes into the database
        saved = await self.save_project_codes(self.project_code, html_code, css_code, js_code)

        # Notify the client about the result
        if saved:
            response = {'message': 'Changes saved successfully'}
        else:
            response = {'message': 'Failed to save changes. Project not found.'}

        await self.send(text_data=json.dumps(response))

    @sync_to_async
    def save_project_codes(self, project_code, html, css, js):
        try:
            # Attempt to find the project by its code and update it
            from main.models import ProjectList
            project = ProjectList.objects.get(project_code=project_code)
            project.html_code = html
            project.css_code = css
            project.js_code = js
            project.save()
            return True
        except ObjectDoesNotExist:
            # Return False if the project does not exist
            return False
