import abc
import pytest

from ..class_registry import AbstractClassRegistry, ClassRegistrationError


@pytest.mark.unit
def test_class_manager():

    class Base:
        pass

    class Registry(AbstractClassRegistry):
        base_classes = [Base]

    class Class1(Base):
        pass

    class Class2(Base, abc.ABC):
        pass

    class Class3:
        pass

    registry = Registry(raise_if_exists=True)
    registry.register_class(Class1)

    # should raise on duplicate class
    with pytest.raises(ClassRegistrationError):
        registry.register_class(Class1)

    # should raise on abstract class
    with pytest.raises(ClassRegistrationError):
        registry.register_class(Class2)
    assert registry.can_register(Class2) is False

    # should raise on wrong bases class
    with pytest.raises(ClassRegistrationError):
        registry.register_class(Class3)
    assert registry.can_register(Class3) is False

    # access registered classes
    assert registry['Class1'] is Class1
    assert registry.Class1 is Class1
    assert 'Class1' in registry
    assert Class1 in registry
    for cls in registry:
        assert issubclass(registry[cls], Base)

    # check namespace registration
    registry = Registry()
    registry.register_classes_from_namespace(locals())
    assert registry.Class1 is Class1

    # test dictionary handling
    namespace = dict(registry)
    assert 'Class1' in namespace
