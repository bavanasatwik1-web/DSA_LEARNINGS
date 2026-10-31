select  MAX(DISTINCT salary) as secondHighestSalary from (select salary, dense_rank()
over(order by salary DESC)AS W from employee)m where W=2;

