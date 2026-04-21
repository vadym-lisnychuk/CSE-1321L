import java.util.Scanner;

class Lab13A{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String[] meals = {
            "Hummus and veggie wrap",
            "Veggie stir fry with tofu",
            "Chicken salad wrap",
            "Grilled chicken with vegetables",

            "Cheese quesadilla",
            "Mac and cheese",
            "Ham and Cheese sandwich",
            "Pasta with meat sauce",

            "Fruit and yogurt bowl",
            "Tomato soup with bread",
            "Yogurt with granola and honey",
            "Egg drop soup with rice"
        };

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

        System.out.println(isVegan);
        // 1 - healthy, 2 - comfort, 3 - light snack
        int index = 0;
        switch (mood) {
            case 1:
                break;
            case 2:
                index += 4;
                break;
            case 3:
                index += 8;
                break;
            default:
                break;
        }

        if (isVegan){
            if(isQuick)
                index += 0;
            else
                index += 1;
        }
        else {
            if(isQuick)
                index += 2;
            else
                index += 3;
        }

        System.out.print("You should try " + meals[index]);
        scanner.close();
    }
}