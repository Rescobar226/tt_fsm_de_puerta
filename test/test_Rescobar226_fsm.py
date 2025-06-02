from tt_test import BaseTestCase

class TestFSM(BaseTestCase):
    def test_fsm_secuencia(self):
        self.poke("ena", 1)
        self.poke("clk", 0)
        self.poke("rst_n", 0)
        self.step()  # reset

        self.poke("rst_n", 1)
        self.step()  # salir de reset

        # Estado s0 (0001), condiciones: S=1, LC=1
        self.set_ui(0b1001)  # LC=1, S=1
        self.toggle_clk()
        self.expect_uo(0b00000001)  # MA=1, MC=0, s0=1

        # Estado s1 (0010), condiciones: LA=1
        self.set_ui(0b0100)  # LA=1
        self.toggle_clk()
        self.expect_uo(0b00000100)  # MA=0, MC=0, s1=1

        # Estado s2 (0100), condiciones: S=0, LA=1
        self.set_ui(0b0100)  # LA=1, S=0
        self.toggle_clk()
        self.expect_uo(0b00001000)  # MA=0, MC=1, s2=1

        # Estado s3 (1000), condiciones: SE=1
        self.set_ui(0b0010)  # SE=1
        self.toggle_clk()
        self.expect_uo(0b00000001)  # MA=1, MC=0, s0=1

        # Otra vez s3 pero con SE=0, LC=1 → volver a idle
        self.set_ui(0b1000)  # LC=1
        self.toggle_clk()
        self.expect_uo(0b00000000)  # MA=0, MC=0, idle

        self.done()
