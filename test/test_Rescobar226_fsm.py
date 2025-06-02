from tt_test import BaseTestCase

class TestFSM(BaseTestCase):
    def test_fsm_puerta(self):
        # Establece señales constantes
        self.poke("rst_n", 0)
        self.poke("ena", 1)
        self.poke("clk", 0)
        self.step()  # reset activo

        self.poke("rst_n", 1)
        self.step()  # salir del reset

        # Estado inicial: Sen=0, SE=0, LA=0, LC=0
        self.set_ui(0b0000)
        self.toggle_clk()
        self.expect_uo(0b00000000)  # MA=0, MC=0

        # Paso 1: Sen=1 → activar sensor de entrada
        self.set_ui(0b0001)
        self.toggle_clk()
        # No esperamos nada aún, solo transiciones

        # Paso 2: LA=0, LC=0, SE=0 → siguiente paso FSM
        self.set_ui(0b0001)  # mantener Sen activo
        self.toggle_clk()

        # Paso 3: simular llegada a LA=1 → puerta abierta
        self.set_ui(0b0100)  # LA = 1
        self.toggle_clk()

        # Paso 4: SE=1 → emergencia
        self.set_ui(0b0010)  # SE = 1
        self.toggle_clk()

        # Paso 5: LC=1 → puerta cerrada
        self.set_ui(0b1000)  # LC = 1
        self.toggle_clk()

        # Terminamos la prueba
        self.done()
