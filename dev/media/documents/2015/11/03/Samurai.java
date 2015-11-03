class Samurai
{
	public int[][] solution = new int[21][21];
	public static void main(String args[])
	{


	}

	public void setSolution(int[][] i)
	{
		solution = i;
	}
	public int[][] getSolution()
	{
		return solution;
	}

	void solve(int[][] puzzle)
	{


		DancingLinks dl = new DancingLinks(puzzle);


		report(puzzle);


		dl.solve(this);

	}


	int[][] report(int[][] solutions)
	{
		for (int r = 0; r < PUZZLE_SIDE; r++)
		{
			for (int c = 0; c < PUZZLE_SIDE; c++)
				if (solution[r][c] > 0)
					System.out.print(solution[r][c] + " ");

				else
					System.out.print(". ");

			System.out.println();
		}


		System.out.println("-----------------------------------------");
		return solutions;
	}


	static final int PUZZLE_SIDE = 21;
	static final int PUZZLE_SIZE = 441;
	static final int SUDOKU_SIDE = 9;
	static final int SUDOKU_SIZE = 81;
	static final int SQUARE_SIDE = 3;
	static final int COLUMN_SIZE = 1692;



	static final int[][] SAMURAI_SQUARE = 
		{{0}, {0},    {0},  {},    {1}, {1}, {1},
		{0}, {0},    {0},  {},    {1}, {1}, {1},
		{0}, {0}, {0, 2}, {2}, {1, 2}, {1}, {1},
		{},  {},    {2}, {2},    {2},  {},  {},
		{3}, {3}, {2, 3}, {2}, {2, 4}, {4}, {4},
		{3}, {3},    {3}, {},     {4}, {4}, {4},
		{3}, {3},    {3}, {},     {4}, {4}, {4}};

	static final int[][] SUDOKU_ROW =
		{{0, 1, 2, 3, 4, 5, 6, 7, 8},
		{0, 1, 2, 3, 4, 5, 6, 7, 8},
		{-1,-1,-1,-1,-1,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8},
		{-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8},
		{-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8}};

	static final int[][] SUDOKU_COLUMN =
		{{0, 1, 2, 3, 4, 5, 6, 7, 8},
		{-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8},
		{-1,-1,-1,-1,-1,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8},
		{0, 1, 2, 3, 4, 5, 6, 7, 8},
		{-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8}};



	class DancingLinks
	{
		Samurai samurai;
		boolean stop;
		int[] stats;
		int index;
		Column h;
		Node[] o;


		DancingLinks(int[][] p)
		{

			h = new Column(null, 0);
			Column[] m = new Column[COLUMN_SIZE];


			for (int i = 0; i < COLUMN_SIZE; i++)
				m[i] = new Column(h, 0);


			Node[] l = new Node[PUZZLE_SIZE];
			int i = 0;


			for (int r = 0; r < PUZZLE_SIDE; r++)
				for (int c = 0; c < PUZZLE_SIDE; c++)
					for (int d = 0; d < SUDOKU_SIDE; d++)
					{


						int k = 1 + (r * PUZZLE_SIDE * SUDOKU_SIDE) +
								(c * SUDOKU_SIDE) + d;


						int s = (c / 3) + ((r / 3) * 7); //where in the big square we at



						if (SAMURAI_SQUARE[s].length > 0)
						{


							Node n = new Node(m[(r * PUZZLE_SIDE) + c], k);


							for (int j = 0; j < SAMURAI_SQUARE[s].length; j++)
							{

								int pz = SAMURAI_SQUARE[s][j]; //which puzzle we in for each slot

								//find the row and col of the puzzle
								int pr = SUDOKU_ROW[pz][r];
								int pc = SUDOKU_COLUMN[pz][c];



								n.add(new Node(m[PUZZLE_SIZE +
								                 (pz * SUDOKU_SIZE) +
								                 (pr * SUDOKU_SIDE) + d], k)); //make a node that has row, digit, 

								// Add a node for the puzzle, column
								// and digit.

								n.add(new Node(m[PUZZLE_SIZE + 405 +
								                 (pz * SUDOKU_SIZE) +
								                 (pc * SUDOKU_SIDE) + d], k));
							}



							n.add(new Node(m[PUZZLE_SIZE + 405 + 405 +
							                 (s * SUDOKU_SIDE) + d], k));

							if (p[c][r] == (d + 1))
								l[i++] = n;
						}
					}


			for (Column c = (Column) h.r; c != h; c = (Column) c.r)
				if (c.s == 0)
					c.cover();


			o = new Node[PUZZLE_SIZE]; //output array


			for (int j = 0; j < i; j++)
			{
				l[j].remove();
				o[index++] = l[j];
			}


			stats = new int[PUZZLE_SIZE];
		}


		int[][] report(int[] o)
		{
			// Create an array for the result.

			int a[][] = new int[PUZZLE_SIDE][PUZZLE_SIDE];

			// Convert the row number back to row, column, digit.

			for (int i = 0; i < o.length; i++)
			{
				int v = o[i];

				int d = v % SUDOKU_SIDE;
				int c = (v / SUDOKU_SIDE) % PUZZLE_SIDE;
				int r = (v / (PUZZLE_SIDE * SUDOKU_SIDE)) % PUZZLE_SIDE;

				a[c][r] = d + 1;
			}

			// Report the result.

			samurai.report(a);
			setSolution(a);

			// Create an array for the stats

			int s[][] = new int[PUZZLE_SIDE][PUZZLE_SIDE];

			for (int i = 0; i < o.length; i++)
				s[i / PUZZLE_SIDE][i % PUZZLE_SIDE] = stats[i];

			// Report stats.

			samurai.report(s);
			return a;

		}

		// Start the search process.

		void solve(Samurai s)
		{
			samurai = s;
			search(index);
		}

		// This is the procedure search(k) from the Dancing Links
		// algorithm with an added feature to report only one
		// solution.

		void search(int k)
		{
			// If a result has already been found, return.

			if (stop)
				return;

			// If there are no more columns, report the result.

			if (h.r == h)
			{
				int[] a = new int[k];

				// Extract the row numbers.

				for (int i = 0; i < k; i++)
					a[i] = o[i].n - 1;

				// Report the result and set the stop flag.

				report(a);
				stop = true;
			}

			// Else find the shortest column and cover it.

			else
			{
				Column c = null;
				int s = Integer.MAX_VALUE;

				// Increment stats;

				stats[k]++;

				// Find the shortest column.

				for (Column j = (Column) h.r; j != h; j = (Column) j.r)
					if (s > j.s)
					{
						c = j;
						s = j.s;
					}

				// Cover it.

				c.cover();

				// For each row in the column...

				for (Node r = c.d; r != c; r = r.d)
				{
					// Skip this if a result has been found.

					if (stop)
						break;

					// Save the row in the output array.

					o[k] = r;

					// For each node in this row, cover it's column.

					for (Node j = r.r; j != r; j = j.r)
						j.c.cover();

					// Recurse with k + 1.

					search(k + 1);

					// For each node in this row, uncover it's column.

					for (Node j = r.l; j != r; j = j.l)
						j.c.uncover();
				}


				c.uncover();
			}
		}
	}



	class Node
	{
		Node l;
		Node r;
		Node u;
		Node d;
		Column c;
		int n;


		Node(Column c, int n)
		{
			this.l = this;
			this.r = this;

			this.u = this;
			this.d = this;


			this.c = c;
			this.n = n;


			if (c != null)
				c.add(this);
		}


		void remove()
		{
			Node n = this;


			do
			{
				n.c.cover();
				n = n.r;
			}


			while (n != this);
		}


		void add(Node n)
		{
			n.l = this.l;
			n.r = this;

			this.l.r = n;
			this.l = n;
		}
	}



	class Column extends Node
	{
		int s;


		Column(Column c, int n)
		{
			super(null, n);

			if (c != null)
				c.add(this);
		}


		void cover()
		{

			r.l = l;
			l.r = r;


			for (Node i = d; i != this; i = i.d)



				for (Node j = i.r; j != i; j = j.r)
				{

					j.u.d = j.d;
					j.d.u = j.u;


					j.c.s--;
				}
		}



		void uncover()
		{

			for (Node i = u; i != this; i = i.u)



				for (Node j = i.l; j != i; j = j.l)
				{

					j.u.d = j;
					j.d.u = j;


					j.c.s++;
				}


			r.l = this;
			l.r = this;
		}


		void add(Column c) //add node to left of col
		{
			c.l = this.l;
			c.r = this;

			this.l.r = c;
			this.l = c;
		}


		void add(Node n) //add node end of column
		{
			n.u = this.u;
			n.d = this;

			this.u.d = n;
			this.u = n;

			s++; //column size goes up
		}
	}
}

