
public class Cell {
	public Cell left;
	public Cell right;
	public Cell up;
	public Cell down;
	Col myCol;
	int row;

	public Cell(Col c, int r)
	{
		row = r;
		left = this;
		right = this;
		up = this;
		down = this;

		myCol = c;

		if(myCol != null)
		{
			myCol.add(this);
		}


	}
	public void delete()
	{

		myCol.cover();
		Cell newCell = right;
		while(newCell != this)
		{
			newCell.myCol.cover();
			newCell = newCell.right;
		}
	}
	public void addNew(Cell c) //add 
	{
		c.left = this.left;
		c.right = this.right;

		this.left.right = c; //put that new cell to the right of my left neighbor #squeezeItIn
		this.left = c; //put new cell to left of me
	}
}
