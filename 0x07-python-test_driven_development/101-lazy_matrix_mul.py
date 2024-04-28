import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: Result of matrix multiplication.

    Raises:
        ValueError: If matrices cannot be multiplied due to incompatible shapes.
        TypeError: If either matrix is not a list of lists or if the matrices contain invalid elements.
    """
    try:
        matrix_a = np.array(m_a)
        matrix_b = np.array(m_b)
        result = np.matmul(matrix_a, matrix_b)
        return result.tolist()
    except ValueError as ve:
        raise ValueError("Matrices cannot be multiplied: {}".format(ve))
    except Exception as e:
        raise TypeError("Invalid input: {}".format(e))
