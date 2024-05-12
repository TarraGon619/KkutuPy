from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
rooms = []

@csrf_exempt
def lobby(req):
    if req.method == "GET":
        return render(req, 'main/index.html', {'rooms':rooms})
    elif req.method == 'POST':
        d = list(req.POST.values())
        if d[0] == '':
            if d[5] == '':
                d[5] = 'guest'
            d[0] = f'{d[5]}님의 방'
        rooms.append(d)
        print(rooms)

        if req.POST['roomName'] == "d":
            rooms.clear()

        # return render(req, 'main/index.html', {'rooms':rooms})
        return render(req, 'main/index.html', {'Rname':d[0], 'Rmax':d[2], 'Rround':d[3], 'Rtime':d[4]})