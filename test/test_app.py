import pytest
from app import create_app, db
from app.models import Owner, Car

@pytest.fixture
def app():
    app = create_app()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    owner1 = Owner(name="John Doe")
    owner2 = Owner(name="Jane Doe")
    db.session.add(owner1)
    db.session.add(owner2)
    db.session.commit()
    yield db
    db.session.remove()

# Teste para adicionar um proprietário
def test_add_owner(client):
    response = client.post('/owners', json={"name": "Test Owner"})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Owner added successfully'

# Teste para listar proprietários
def test_get_owners(client, init_database):
    response = client.get('/owners')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2  
    assert data[0]['name'] == 'John Doe'

def test_add_car(client, init_database):
    response = client.post('/owners/1/cars', json={"model": "sedan", "color": "blue"})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Car added successfully'

def test_add_car_limit(client, init_database):
    client.post('/owners/1/cars', json={"model": "sedan", "color": "blue"})
    client.post('/owners/1/cars', json={"model": "hatch", "color": "yellow"})
    client.post('/owners/1/cars', json={"model": "convertible", "color": "gray"})

    response = client.post('/owners/1/cars', json={"model": "sedan", "color": "blue"})
    assert response.status_code == 400
    assert response.get_json()['message'] == 'Owner cannot have more than 3 cars'
