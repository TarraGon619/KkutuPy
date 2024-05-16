from django.shortcuts import render, redirect
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
        D.update({'id':len(rooms)+1})
        room_id = D['id']
        # D['id'] = len(rooms)+1
        if D['roomName'] == '':
            if D['name'] == '':
                D['name'] = 'guest'
            D['roomName'] = D['name']+'님의 방'

        rooms.append(D)
        print("방 수", len(rooms))

        if req.POST['roomName'] == "d":
            rooms.clear()

        return redirect(f'room/{room_id}/')
        # return render(req, 'main/index.html', {'rooms':rooms})

def room(req, room_id):
    return render(req, 'main/room.html', {'room_id':room_id})
