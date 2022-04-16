from PyQt5.QtWidgets import QStackedWidget

from screens.Materials.MainMaterialsScreen import MainMaterialsScreen

MaterialsNavigator = QStackedWidget()

MainMaterials = MainMaterialsScreen()

MaterialsNavigator.addWidget(MainMaterials)

MaterialsNavigator.setCurrentWidget(MainMaterials)
