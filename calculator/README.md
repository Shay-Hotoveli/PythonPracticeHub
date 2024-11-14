# Calculator Program

This is a Python-based calculator that supports a variety of operations, including addition, subtraction, multiplication, division, modulus, exponentiation, and floor division. Additionally, it allows users to log calculations, view stored calculations, and clear logs through a straightforward menu-driven interface.

## Planned Improvements

1. **Refactor `calculate` function for improved readability**  
   Replace the `match/case` statement with a dictionary that maps operations to functions. This will make it easier to add new operations in the future.

2. **Improve `view_calculations` function**  
   Add an empty log check to avoid printing when there is no content in the log file.

3. **Add an option to exit input with "q"**  
   Allow users to type `"q"` during number or operation input to return to the main menu.

4. **Enhance menu visual appeal**  
   Improve the organization and visual design of the main menu to enhance user experience and navigation clarity.

5. **Add continuous calculation functionality**  
   Enable users to perform additional calculations on the previous result, similar to the "Ans" feature on physical calculators.

6. **Update calculation output**  
   Modify the output format to show the full calculation (e.g., `5 + 3 = 8` instead of just `8`).

7. **Enhance `view_calculations` output formatting**  
   Organize log entries neatly and add options for controlling the output display (e.g., showing only the last 5 entries).

---

These improvements aim to make the calculator more user-friendly, maintainable, and visually appealing. Happy calculating!
