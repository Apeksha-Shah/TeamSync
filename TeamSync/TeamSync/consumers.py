import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist

class CodeEditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_code = self.scope['url_route']['kwargs']['project_code']
        self.project_group_name = 'project_%s' % self.project_code

        # Join project group
        await self.channel_layer.group_add(
            self.project_group_name,
            self.channel_name
            
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave project group
        await self.channel_layer.group_discard(
            self.project_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        html_code = text_data_json['html_code']
        css_code = text_data_json['css_code']
        js_code = text_data_json['js_code']

        saved = await self.save_project_codes(self.project_code, html_code, css_code, js_code)

        if saved:
            # Broadcast the update to all clients in the project group
            await self.channel_layer.group_send(
                self.project_group_name,
                {
                    'type': 'broadcast_code_update',
                    'html_code': html_code,
                    'css_code': css_code,
                    'js_code': js_code,
                }
            )

    async def broadcast_code_update(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'html_code': event['html_code'],
            'css_code': event['css_code'],
            'js_code': event['js_code'],
            'message': 'Code updated'
        }))

    @sync_to_async
    def save_project_codes(self, project_code, html, css, js):
        try:
            from main.models import ProjectList
            project = ProjectList.objects.get(project_code=project_code)
            project.html_code = html
            project.css_code = css
            project.js_code = js
            project.save()
            return True
        except ObjectDoesNotExist:
            return False
