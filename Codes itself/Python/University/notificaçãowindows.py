# Isso aqui tá salvo no instagram.
from win10toast import ToastNotifier
#Inicializar:
toaster = ToastNotifier()

# Passa os parametros e mostra a notificação
toaster.show_toast(
    "Notificação",
    "Acabou o contador.",
    threaded = True,
    icon_path = None,
    duration = 2
)