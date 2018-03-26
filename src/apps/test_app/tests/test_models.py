
import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestPost:
    def test_model(self):
        obj = mixer.blend("apps.test_app.models.Post")
        assert obj.pk == 1, "Asi deberias crear una instancia de Post"