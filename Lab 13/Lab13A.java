import java.util.Scanner;

class Lab13A{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("[Meal Selector]");
        
        System.out.print("How many minutes do you have to prep your meal?: ");
        int minutes = scanner.nextInt();
        scanner.nextLine(); 

        System.out.print("What is your mood?:\n1. Healthy\n2. Comfort\n3. Light Snack\n> ");
        int mood = scanner.nextInt();
        scanner.nextLine(); 

        System.out.print("Vegetarian option? (true/false): ");
        String vegan = scanner.nextLine();

        boolean isVegan = (vegan.equals("true"));
        boolean isQuick = (minutes <= 15);

        // 1 - healthy, 2 - comfort, 3 - light snack
        String meal = "";
        switch (mood) {
            case 1:
                if(isVegan)
                    if(isQuick)
                        meal += "Hummus and veggie wrap";
                    else
                        meal += "Veggie stir fry with tofu";
                else 
                    if(isQuick)
                        meal += "Chicken salad wrap";
                    else
                        meal += "Grilled chicken with vegetables";
                break;
            case 2:
                if(isVegan)
                    if(isQuick)
                        meal += "Cheese quesadilla";
                    else
                        meal += "Mac and cheese";
                else 
                    if(isQuick)
                        meal += "Ham and Cheese sandwich";
                    else
                        meal += "Pasta with meat sauce";
                break;
            case 3:
                if(isVegan)
                    if(isQuick)
                        meal += "Fruit and yogurt bowl";
                    else
                        meal += "Tomato soup with bread";
                else 
                    if(isQuick)
                        meal += "Yogurt with granola and honey";
                    else
                        meal += "Egg drop soup with rice";
                break;
            default:
                break;
        
        }
        System.out.print("You should try " + meal);
        scanner.close();
    }
}