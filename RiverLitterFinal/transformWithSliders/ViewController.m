//
//  ViewController.m
//  transformWithSliders
//
//  Created by Abraham Avnisan on 4/10/16.
//  Copyright © 2016 Abraham Avnisan. All rights reserved.
//

#import "ViewController.h"
#import "FactsViewController.h"
//#import "ScoreViewController.h"

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UILabel *scoreLabel;
@property (nonatomic) int score;
@property (weak, nonatomic) IBOutlet UILabel *liveLabel;
@property (nonatomic) int lives;
@property (weak, nonatomic) IBOutlet UILabel *gameOverLabel;
@property (weak, nonatomic) IBOutlet UIImageView *gameOverButton;
@property (weak, nonatomic) IBOutlet UILabel *gameOverText;
@property (weak, nonatomic) IBOutlet UIButton *gameOverFunction;

//@property (int)  highScore;


@end

@implementation ViewController
#pragma mark - setup
- (void)setup
{
    // initialize our properties
    self.scale = 1.0;
    self.scalePrev = 1.0;
    
    self.rotation = 0.0;
    self.rotationPrev = 0.0;
    
    self.translateX = 0.0;
    self.translateXPrev = 0.0;
    self.translateY = 0.0;
    self.translateYPrev = 0.0;
    
    self.garbageObjects = [[NSMutableArray alloc] initWithObjects:self.garbageExample, self.garbageExample2, self.garbageExample3, self.garbageExample4, self.garbageExample5, self.garbageExample6, self.garbageExample7, self.garbageExample8, self.garbageExample9, nil];
    
   // self.highScore = 0;
    
    // update our labels
    [self updateTransform];
//    [self animateGarbage];
}


#pragma mark - update
- (void)updateTransform
{
    CGAffineTransform transform = CGAffineTransformIdentity;
    transform = CGAffineTransformTranslate(transform, self.translateX, self.translateY);
    transform = CGAffineTransformScale(transform, self.scale, self.scale);
    transform = CGAffineTransformRotate(transform, self.rotation);
    
    self.imageView.transform = transform;
    
//    [self updateLabels];
}
//- (void)updateLabels
//{
//    self.translateXLabel.text =     [NSString stringWithFormat:@"translate x: %.2f", self.translateX];
//    self.translateYLabel.text =     [NSString stringWithFormat:@"translate y: %.2f", self.translateY];
//    self.scaleLabel.text =          [NSString stringWithFormat:@"scale: %.2f", self.scale];
//    self.rotationLabel.text =       [NSString stringWithFormat:@"rotation: %.2f", self.rotation];
//}
#pragma mark - actions
- (IBAction)userDidPinch:(UIPinchGestureRecognizer *)sender
{
    if (sender.state == UIGestureRecognizerStateBegan) {
        // this happens at the START of each pinch gesture
        self.scalePrev = self.scale;
    }
    
    // calculate the difference in scale as a percentage
    float scaleDiff = sender.scale - 1.0;
    
    // update the scale by taking the what the scale value
    // was at the START of the pinch gesture and adding a
    // percentage of that initial start value
    self.scale = self.scalePrev + (self.scalePrev * scaleDiff);

    [self updateTransform];
    
}
- (IBAction)userDidRotate:(UIRotationGestureRecognizer *)sender
{
    if (sender.state == UIGestureRecognizerStateBegan) {
        // this happens at the START of each pinch gesture
        self.rotationPrev = self.rotation;
    }
    
    self.rotation = self.rotationPrev + sender.rotation;

    // update transform
    [self updateTransform];
    
}
- (IBAction)userDidPan:(UIPanGestureRecognizer *)sender
{
    float xLocation = [sender locationInView:self.view.superview].x;
    float yLocation = [sender locationInView:self.view.superview].y;
    
    if (yLocation < self.view.frame.size.height / 2.0) {
        yLocation = self.view.frame.size.height / 2.0;
    }

    if (sender.state == UIGestureRecognizerStateBegan) {
        // this happens at the START of each pinch gesture
        self.translateXPrev = self.translateX;
        self.translateYPrev = self.translateY;
        
        self.xStartLocation = xLocation;
        self.yStartLocation = yLocation;
    }
    
    // calculate how much the user has moved their finger
    float xDiff = self.xStartLocation - xLocation;
    float yDiff = self.yStartLocation - yLocation;
    
    // set new translate value
    self.translateX = self.translateXPrev - xDiff;
    self.translateY = self.translateYPrev - yDiff;

    // update transform
    [self updateTransform];

}
- (void)detectCollisions //detects when a garbage object hits the boat (player)
{
    int randomNumber = (int)arc4random_uniform(100 - 50);
    
    for (NSUInteger i = 0; i < self.garbageObjects.count; i++) {
        
        UIImageView *thisGarbageObject = self.garbageObjects[i];
        thisGarbageObject.center = CGPointMake(thisGarbageObject.center.x, thisGarbageObject.center.y + 10);
        
        if (CGRectIntersectsRect(thisGarbageObject.frame, self.imageView.frame)) {
            // remove garbage view
            [thisGarbageObject removeFromSuperview];
            thisGarbageObject.center = CGPointMake(arc4random_uniform(375), randomNumber);
            [self.view addSubview:self.garbageObjects[i]];
            NSLog(@"garbage collected");
            // update score
            self.score++;

//            if (self.highScore < self.score) {
//                self.highScore = self.score;
//            }
//
            NSString *scoreString = [NSString stringWithFormat:@"%i", self.score];
            self.scoreLabel.text = scoreString;
        }
    }
}

-(void)GameOver{ //in place of a game over screen, this hides the game over "overlay" until the user runs out of lives. It then freezes the loop and shows itself.
    [garbageMovementTimer invalidate];
    self.imageView.hidden = YES;
    self.gameOverLabel.hidden = NO;
    self.gameOverText.hidden = NO;
    self.gameOverButton.hidden = NO;
    self.gameOverFunction.hidden = NO;
}

-(void) garbageAnimate{ //this animates the garbage and pulls them from the array
    int randomNumber = (int)arc4random_uniform(100 - 50);

    for (NSUInteger i = 0; i < self.garbageObjects.count; i++) {

        UIImageView *thisGarbageObject = self.garbageObjects[i];
        thisGarbageObject.center = CGPointMake(thisGarbageObject.center.x, thisGarbageObject.center.y);

        if (CGRectIntersectsRect(thisGarbageObject.frame, self.border.frame)) {
            thisGarbageObject.center = CGPointMake(arc4random_uniform(375), randomNumber);
            [self.view addSubview:self.garbageObjects[i]];
            // lives
            self.lives--;
            NSString *liveString = [NSString stringWithFormat:@"%i", self.lives];
            self.liveLabel.text = liveString;
            
            if(self.lives == 0){
                [self GameOver];
            }
        }
    }
    [self detectCollisions];
}

#pragma mark - inherited methods
- (void)viewDidLoad {

    self.gameOverLabel.hidden = YES;
    self.gameOverText.hidden = YES;
    self.gameOverButton.hidden = YES;
    self.gameOverFunction.hidden = YES;
    
    garbageMovementTimer = [NSTimer scheduledTimerWithTimeInterval:0.04 target:self selector:@selector(garbageAnimate) userInfo:nil repeats:YES];
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    [self setup];
    self.score = 0;
    self.lives =10;
}

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    FactsViewController *factsVC = (FactsViewController *)segue.destinationViewController;
    factsVC.userScore = self.scoreLabel.text.intValue;
}

@end

