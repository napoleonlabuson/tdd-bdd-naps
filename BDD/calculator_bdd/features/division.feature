Feature: dividing two numbers

   Scenario: when dividing two integers
     Given two valid integers
      When dividing the integers
      Then it should result to another integer
      
    Scenario: when dividing zero to a nonzero integer
      Given integer and zero
      When dividing zero to an integer
      Then it should result to zero
      
    Scenario: when dividing a nonzero integer to zero
      Given zero and integer
      When dividing an integer to zero
      Then it should result to undefined