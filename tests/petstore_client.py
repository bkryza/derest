from derest import RestClient
from derest import GET, POST, PUT, DELETE
from derest import header, query


class PetstoreClient(RestClient):
    def __init__(self, endpoint, auth):
        super(PetstoreClient, self).__init__(endpoint, auth)

    @POST('pet')
    @header('content-type', 'application/json')
    def add_pet(self, pet):
        """Add a new pet to the store"""

    @PUT('pet')
    def update_pet(self, pet):
        """Update an existing pet"""

    @GET('pet/findByStatus')
    def find_pet_by_status(self):
        """Finds Pets by status"""

    @GET('pet/findByStatus')
    @header('accept', 'application/xml')
    def find_pet_by_status_xml(self):
        """Finds Pets by status"""

    @GET('pet/{pet_id}')
    def find_pet_by_id(self, pet_id):
        """Find Pet by ID"""

    @POST('pet/{pet_id}')
    def update_pet_by_id(self, pet_id):
        """Updates a pet in the store with form data"""

    @DELETE('pet/{pet_id}')
    def delete_pet(self, pet_id):
        """Deletes a pet"""

    @POST('pet/{pet_id}/uploadImage')
    def upload_pet_image(self, pet_id, image):
        """uploads an image"""
