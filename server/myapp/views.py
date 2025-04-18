from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def signup(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    print(f"Received: {name}, {email}, {password}")  # Debug line

    if not all([name, email, password]):
        return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

    # ... your user creation logic here ...
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
