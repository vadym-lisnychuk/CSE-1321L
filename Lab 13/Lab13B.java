import java.util.Scanner;

class Lab13B{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        while(true){
        System.out.println("Enter your lab grades:");
        int n = 13;
        float current_grade;
        float min_grade = 0;
        float sum = 0;
        for(int i = 0; i < n; i++){
            System.out.print(String.format("Lab %d: ", i + 1));
            current_grade = scanner.nextFloat();
            scanner.nextLine();

            sum += current_grade;
            if(i == 0)
                min_grade = current_grade;
            
            if(current_grade < min_grade)
                min_grade = current_grade;
        }
        System.out.println(String.format("The lowest lab grade was: %f", min_grade));
        System.out.println(String.format("Your lab grade average is: %f", sum / 13));
        System.out.println(String.format("Your lab grade average after policy is : %f", (sum - min_grade)/ 12));
        System.out.print("Do you want to try again? (Y/N): ");
        String cont = scanner.nextLine();

        if(cont.equals("N"))
            break;

        }
        scanner.close();

    }
}