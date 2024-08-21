// Learning this thing.

/*To coment things
 * In multiple Lines
 * we do like this, puitting an asterisk and a bar like it is here
 * Easy
 */

/* Variables in java: String, int, float, char, boolean
To create a variable we do like this: type variableName = value; 
where type is the type of the variable, like a String, int, etc; variableName is the name of the variable 
and value, obviously, is the value, can be a name, a number or something like that.
*/

public class Main {
    public static void main(String[] args){
        String firstName = "Carlos ";
        String secondName = "Hirai";
        String name = firstName + secondName; // Here we putted two names together, saying that it's the first and second name, remember to put a space after the first one.
        /*float x = 1f;
        float y = 1.5f;
        float sum = (x + y); // adding two values, used float values to not get an error when doing the operation.
        float num = 1.6f; // FOR SOME REASON FOR THE FLOAT VALUE, HAS TO BE AN f AT THE END OF THE VALUE */
        int num_int = 2; // Here is a normal thing. 
        float x = 1f, y = 1.5f, sum = (x + y), num =  1.6f; /*Instead of writting like we did right above us, we can write like this
        It's more organizated, clean, and save us time. REMEMBER to put a comma "," between the new values and a ";" on the last one. */
        /* int x,y,z;
        * x = y = z = 50;  We do like this if we want to declare the same value to multiple variables. */
        char myChar = 'R'; // creating a char type variable, which we select a character, IT HAS TO BE INSIDE AN SINGLE PAIR OF COMMA ''.
        boolean myBool = true; // creating a boolean variable, we just put true or false, nothing else.
        System.out.println("Muito quente"); // Always remember to put the ; (point and comma) when finishing a command or something like
        System.out.println(300); // for some reason that the devil wanted, isn't needed to put double comma "" when we are trying to print a number, but you can.
        System.out.println(300+50); // to perform mathematical stuff, we can do it inside the (), at least this.
        System.out.println(300*2);
        System.out.println(name); // here we created a variable called name, which stores a name, and it has to be inside the main().
        System.out.println(num);
        System.out.println(num_int);
        System.out.println(myChar);
        System.out.println("Oi," + name);
        System.out.println(sum);
    }
}