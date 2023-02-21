#Create and transform vectors and matrices (the transpose vector (matrix) conjugate transpose of a vector (matrix)) 

import numpy as np
v = np.array([1, 2, 3, 4])
print(v)
import numpy as np
M = np.array([[1, 2, 3], [4, 5, 6]])
print(M)
import numpy as np
v = np.array([1, 2, 3, 4])
v_T = v.T
print(v_T)
import numpy as np
M = np.array([[1, 2, 3], [4, 5, 6]])
M_T = M.T
print(M_T)
import numpy as np
v = np.array([1, 2, 3, 4])
v_H = v.conj().T
print(v_H)
import numpy as np
M = np.array([[1+2j, 2+3j, 3+4j], [4+5j, 5+6j, 6+7j]])
M_H = M.conj().T
print(M_H)
