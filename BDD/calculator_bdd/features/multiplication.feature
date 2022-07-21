Feature: multiplying two numbers

  Scenario: when multiplying two integers
     Given two valid integers
      When multiplying the integers
      Then it should result to another integer
      
    Scenario: when multiplying zero to an integer
      Given an integer and a zero
      When multiplying zero to an integer
      Then it should result to zero