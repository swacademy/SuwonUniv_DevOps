class Student :
    def __init__(self, hakbun, name, kor, eng, math, edps):  
        """Student class의 Constructor"""
        self.hakbun = hakbun
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.edps = edps 
        
    def __str__(self) :
        """Student Print"""
        return f'{self._hakbun:<10s}\t{self._name:10s}\t' + \
            f'{self._kor:5d}\t{self._eng:5d}\t{self._math:5d}\t{self._edps:5d}\t' + \
            f'{self._tot:10d}\t{self._avg:10.2f}\t{self._grade:5s}'    
        
    @property
    def hakbun(self): return self._hakbun
    @property
    def name(self): return self._name
    @property
    def kor(self):return self._kor
    @property
    def eng (self):return self._eng
    @property
    def math (self):return self._math
    @property
    def edps (self):return self._edps
    @property
    def tot(self):return self._tot
    @property
    def avg(self):return self._avg
    @property
    def grade(self):return self._grade
    @hakbun.setter
    def hakbun(self, hakbun): self._hanbun = hakbun
    @name.setter
    def name(self, name): self._name = name
    @kor.setter
    def kor(self, kor): self._kor = kor
    @eng.setter
    def eng(self, eng): self._eng = eng
    @math.setter
    def math(self, math): self._math = math
    @edps.setter
    def edps(self, edps): self._edps = edps
    @tot.setter
    def tot(self, tot): self._tot = tot
    @avg.setter
    def avg(self, avg): self._avg = avg
    @grade.setter
    def grade(self, grade): self._grade = grade 