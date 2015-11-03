import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Panel;
import java.awt.geom.Line2D;
import java.util.ArrayList;

import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JRadioButton;

public class App {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		App n = new App();

	}

	public App() {
		JFrame frame = new JFrame();

		frame.setBounds(250, 250, 300, 280); // Can adjust the size of the frame
												// here

		Panel jPanel = new Panel();

		ArrayList<JRadioButton> buttonList = new ArrayList<JRadioButton>();

		ButtonGroup bg = new ButtonGroup();

		for (int i = 0; i < 9; i++) {

			for (int j = 0; j < 9; j++) {

				// String buttonName = "(" + (i + 1) + ", " + (j + 1) + ")";

				JRadioButton button = new JRadioButton();
				
				button.setBackground(Color.BLACK);

				button.setBounds(i * 10, j * 10, 10, 10);

				jPanel.add(button);

				buttonList.add(button);

				bg.add(button);

			}
		}

		frame.add(jPanel);
		frame.setVisible(true);

		// super.paintComponent(g);
		//
		// for (int i = 0; i <= 540; i += 60) {
		// g.drawLine(i, 0, i, 540);
		// }
		//
		// for (int i = 0; i <= 540; i += 60) {
		// g.drawLine(0, i, 540, i);
		// }
		//
		// // change line thickness to draw bigger board
		// Graphics2D g2 = (Graphics2D) g;
		// g2.setStroke(new BasicStroke(5));
		//
		// for (int i = 180; i < 540; i += 180) {
		// g2.draw(new Line2D.Float(i, 0, i, 540));
		// }
		//
		// for (int i = 180; i < 540; i += 180) {
		// g2.draw(new Line2D.Float(0, i, 540, i));
		// }
	}
}
