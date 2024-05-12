from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
rooms = []

@csrf_exempt
def lobby(req):
    if req.method == "GET":
        return render(req, 'main/index.html', {'rooms':rooms})
    elif req.method == 'POST':
        # d = list(req.POST.values())
        # if d[0] == '':
        #     if d[5] == '':
        #         d[5] = 'guest'
        #     d[0] = f'{d[5]}님의 방'
        # rooms.append(d)
        # print(rooms)

        D = req.POST.copy()
        if D['roomName'] == '':
            if D['name'] == '':
                D['name'] = 'guest'
            D['roomName'] = D['name']+'님의 방'

        rooms.append(D)
        print("방 수", len(rooms))

        if req.POST['roomName'] == "d":
            rooms.clear()

        return render(req, 'main/index.html', {'rooms':rooms})
        # return render(req, 'main/index.html', {'rooms':rooms, 'Rname':d[0], 'Rmax':d[2], 'Rround':d[3], 'Rtime':d[4]})