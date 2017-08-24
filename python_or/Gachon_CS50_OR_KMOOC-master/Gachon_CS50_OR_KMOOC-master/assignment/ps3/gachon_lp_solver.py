import numpy as np


class GachonLPSolver:
    MAXIMIZE = 0
    MINIMIZE = 1
    LESSEQUAL = 1
    EQUAL = 0
    GRATERQUAL = -1

    def __init__(self, model_name):
        self._model_name = model_name
        self._objective_variables = None
        self._optimize_setting = None
        self._standard_form_matrix = None
        self._constraints_coefficient_matrix = None
        self._constraints_sign_list = []
        self._basic_variables_index = None
        self._non_basic_variables_index = None

    def set_objective_variables(self, objective_coefficient_vector, optimize_setting):
        self._objective_variables = np.array(objective_coefficient_vector)
        self._optimize_setting = optimize_setting


    def add_constraints(self, constraints_coefficient_vector, sign, rhs):
        self._constraints_sign_list.append(sign)
        temp_vector = np.array(constraints_coefficient_vector + [rhs])

        if self._constraints_coefficient_matrix is None:
            self._constraints_coefficient_matrix = temp_vector
        else:
            self._constraints_coefficient_matrix = np.vstack([self._constraints_coefficient_matrix,
                                                    temp_vector])

    def update(self):
        obj_var_len = self._objective_variables.shape[0]
        cons_row_len = self._constraints_coefficient_matrix.shape[0]


        strand_matrix_col_len  = 1 + obj_var_len + cons_row_len
        strand_matrix_row_len= 1 + cons_row_len

        for row_vector_index in range(strand_matrix_row_len) :
            temp_vector = np.array([])

            if row_vector_index == 0:
                temp_vector = np.array( [1] + (-self._objective_variables).tolist() + [0] * (cons_row_len + 1))
            else:
                temp_vector = np.array(
                                [1] +
                                self._constraints_coefficient_matrix[row_vector_index - 1][0:-1].tolist() +
                                np.eye(cons_row_len)[row_vector_index-1].tolist() +
                                [self._constraints_coefficient_matrix[row_vector_index - 1][-1]]
                                )

            if self._standard_form_matrix is None:
                self._standard_form_matrix = temp_vector
            else:
                self._standard_form_matrix = np.vstack([self._standard_form_matrix,
                                                        temp_vector])


    def optimize(self):

        self._basic_variables_index = None
        self._non_basic_variables_index = None

        # self._standard_form_matrix
        # gauss_jordan_elimination_process()

        # 초기화 nbs = s1, s2, ...  bs = x1,x2...

        # entering variable 선정
        # step 1 find pivot value col_position
        # check first row 에서 최소값이 <0 인지 확인, 최소 값인 column_position 찾아야 함
        # 만약 최소값이 0보다 크면 loop를 빠져 나감

        # exit variable 선정
        # step 2 find pivot value row_position
        #        rhs/x1 한 값이 min인 row_index, 이 때 nbs, bs value 위치 저장

        # step 3 pivot col_position, row_position에 대해 GEP 수행

        # step 4 first row(obj vector) 에서 최소값이 <0 인지 확인, 최소값이 col_position 찾기
        # 만약 최소값이 0보다 크면 loop를 빠져 나감


        pass

    def gauss_jordan_elimination_process(self, pivot_row_position, column_position):
        matrix_row_size = self._standard_form_matrix.shape[0]
        pivot_value = self._standard_form_matrix[pivot_row_position, column_position]
        if pivot_value < 0:
            self._standard_form_matrix[pivot_row_position, :] = -1 * self._standard_form_matrix[
                pivot_row_position, column_position]

        for i in range(matrix_row_size):
            if i != pivot_row_position:
                target_value = self._standard_form_matrix[i][column_position]
                compensating_value = -1 * (target_value / pivot_value)
                pivot_row = compensating_value * self._standard_form_matrix[pivot_row_position, :]
                self._standard_form_matrix[i] += pivot_row

    def get_z_value(self):
        pass

    def get_objective_variables(self):
        pass

    @property
    def standard_form_matrix(self):
        return self._standard_form_matrix

    @property
    def model_name(self):
        return self._model_name

    @property
    def objective_variables(self):
        return self._objective_variables

    @property
    def constraints_coefficient_matrix(self):
        return self._constraints_coefficient_matrix

    @property
    def constraints_sign_list(self):
        return self._constraints_sign_list


def model_name():
    # This is a mock test function.Do NOT need to modify it.
    pass

def set_objective_variables():
    # This is a mock test function.Do NOT need to modify it.
    pass

def add_constraints():
    # This is a mock test function.Do NOT need to modify it.
    pass

def update(self):
    # This is a mock test function.Do NOT need to modify it.
    pass

def optimize_easy(self):
    # This is a mock test function.Do NOT need to modify it.
    pass

def optimize_hard(self):
    # This is a mock test function.Do NOT need to modify it.
    pass
