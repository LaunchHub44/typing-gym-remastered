# Plan to build TypingGym

- 2022-07-20 : introducing B key

## Module 4
- 2022-08-02:

  - Meter class
    - Depletes faster than the player types, but refills slightly when correct key is hit
    - If the meter runs out, the sprint is over

  - Score system
     - Score is determined by accuracy and speed

     - Accuracy
       - 10 points first try hit
       - 5 points second try hit
       - 2 points third try hit
       - 1 point if more than three tries were needed

     - Time
       - 20 points if word is spelled within 5 seconds
       - 10 points if word is spelled within 10 seconds
       - 4 points if word is spelled within 15 seconds
       - 0 points if word is spelled after 15 seconds