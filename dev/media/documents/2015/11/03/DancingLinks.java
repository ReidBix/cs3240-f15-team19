import java.util.Arrays;


public class DancingLinks {
	public SudokuSolver solver;
	Cell[] cells;
	Col head;
	int num;

	public static void main(String args[])
	{
		int[][] puzzle1 =
			{{0,0,0,0,0,5,0,0,0, 0,0,0, 0,0,0,0,2,0,6,0,0},
				{0,0,7,3,0,0,9,0,0, 0,0,0, 0,0,0,0,0,3,0,0,5},
				{0,5,0,0,9,0,0,6,3, 0,0,0, 0,0,8,0,0,0,0,4,0},

				{0,8,0,0,7,3,0,0,0, 0,0,0, 0,4,0,3,0,0,8,0,0},
				{0,0,6,2,0,0,8,0,0, 0,0,0, 7,0,0,0,9,0,5,0,0},
				{4,0,0,5,0,0,0,9,0, 0,0,0, 0,0,0,0,5,0,0,7,0},

				{0,3,0,0,5,0, 0,0,0,7,0,0,0,0,0, 0,0,1,0,0,0},
				{0,0,8,0,0,9, 0,3,0,0,4,9,6,8,0, 4,0,0,2,0,0},
				{0,0,9,0,0,0, 0,0,2,0,0,0,0,0,5, 0,0,0,0,8,0},

				{0,0,0,0,0,0, 9,0,0,6,0,0,0,5,0, 0,0,0,0,0,0},
				{0,0,0,0,0,0, 0,6,0,0,0,0,2,0,0, 0,0,0,0,0,0},
				{0,0,0,0,0,0, 0,5,0,0,0,0,7,0,0, 0,0,0,0,0,0},

				{0,0,0,0,3,0, 0,4,0,0,1,5,8,0,0, 0,0,6,0,0,0},
				{0,0,0,9,0,0, 0,2,0,3,0,0,0,9,0, 0,0,4,0,0,6},
				{0,0,2,0,0,0, 0,0,1,0,0,0,0,0,0, 0,0,8,0,2,0},

				{0,0,0,3,0,0,0,5,0, 0,0,0, 0,0,0,0,4,0,3,0,0},
				{7,0,0,0,1,9,0,0,0, 0,0,0, 0,0,0,5,0,0,7,0,0},
				{0,6,0,0,0,0,2,0,0, 0,0,0, 3,5,6,0,0,0,0,8,0},

				{3,0,0,2,9,0,0,7,0, 0,0,0, 0,0,0,2,6,0,0,0,1},
				{0,0,5,0,0,4,0,0,8, 0,0,0, 0,0,3,0,0,5,0,0,0},
				{0,8,0,0,0,0,0,0,0, 0,0,0, 0,7,0,0,0,0,9,0,0}};

		DancingLinks link = new DancingLinks(puzzle1);
	
	}
	public DancingLinks(int[][] board)
	{
		System.out.println("Hi! I'm a link, and I like to dance!");	


		head = new Col(null, 0);
		/**Col[] cols = new Col[1692]; //idk why its that big tbh

		for(int k = 0; k < 1692; k++)
		{
			System.out.println(Arrays.toString(cols));
			cols[k] = new Col(head, 0);

		}

		Cell[] rows = new Cell[21];
		int hi = 0;

		for(int r = 0; r < 21; r++)
			for(int c = 0; c < 21; c++)
				for(int index = 0; index < 9; index++)
				{
					int rowNum = 1 + (r * 21 * 9) +
							(c * 9) + index;

					System.out.println(rowNum);
				}
		 **/

		Cell test = new Cell(head, 0);
		test.addNew(new Cell(head, 0));
		
		System.out.println(head + ", " + head.right);
		System.out.println(test + ", " + test.left);
		
		System.out.println(head.up);



	}





}
