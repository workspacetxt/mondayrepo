from datetime import datetime 
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html=f'''
    <html>
        <body>
            <h1> Hello world</h1>
            <p> time {now}</p>
        </body>
    </html>
    '''
    return HttpResponse(html)