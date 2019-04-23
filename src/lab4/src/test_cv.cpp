#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>




using namespace ros;





void image_callback(const sensor_msgs::Image::ConstPtr& msg)
{


    	cv_bridge::CvImagePtr cv_ptr = cv_bridge::toCvCopy(msg, "bgr8");
    	cv::Mat test_image = cv_ptr->image;

	
	cv::Mat src_gray;
    	cv::cvtColor(test_image, src_gray, CV_BGR2GRAY);

	cv::Mat dst, edges; 	// Create images

    	// Make the destination image the same size and type as input
	dst.create(src_gray.size(), src_gray.type());

    	// Perform gaussian blur on image to eliminate noisy edges
	cv::blur(src_gray, edges, cv::Size(3,3));
	cv::Canny(edges, edges, 50, 150, 3);        // Perform canny edge detection


	// Show image
    	cv::imshow("win1", edges);
	cv::waitKey(1);


	return;

}







int main (int argc, char** argv)
{


    	init(argc, argv, "test_cv");
	NodeHandle n;

	// Create a window in which to display the image
	cv::namedWindow("win1", 0);
    	cv::startWindowThread();


	// Create window transport object
	image_transport::ImageTransport it(n);
    	image_transport::Subscriber sub = it.subscribe("camera/image", 1, image_callback);


	

	while(ok())
	{

		spin();

	}




	return 0;

}
