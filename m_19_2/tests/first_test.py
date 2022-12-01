from m_19_2.app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 12, 8) == 4

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 7, 8) == 15