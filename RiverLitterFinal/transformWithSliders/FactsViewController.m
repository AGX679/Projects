//
//  FactsViewController.m
//  transformWithGesture
//
//  Created by Alan Xu on 12/6/18.
//  Copyright © 2018 Abraham Avnisan. All rights reserved.
//

#import "FactsViewController.h"
#import "ScoreViewController.h"

@interface FactsViewController ()

@property (weak, nonatomic) IBOutlet UILabel *factsView;
@property (strong, nonatomic) NSArray *facts;
@property (weak, nonatomic) IBOutlet UILabel *scoreView;

@end

@implementation FactsViewController


- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    NSString *scoreDisplay = [NSString stringWithFormat:@"%i", self.userScore];
    self.scoreView.text = scoreDisplay;
    
    NSString *fact1 = @"Every year, more than 9,600 pounds of plastic addities are discharged from sewage treatment plants in the Puget Sound region. Thanks to your hard work and effort in cleaning the river, you've helped reduce overall pollution in Seattle! ";
    NSString *fact2 = @"By 2010, more than 521,000 pounds of toxic wayste, including cancer-causing chemicals, developmental toxins and reproductive toxins, were dumped in Washington waterways. Thank you on behalf of Seattle for keeping our water clean!. ";
    NSString *fact3 = @"Disposable wooden chopsticks are bad for the environment because they are stripping asian forests bare. About 4 million trees are torn down because of the chopstick making.";
    NSString *fact4 = @"Exposure to toxins and pollutants threatens the state's $147 million a year commercial and recrestional fish industry as well as the state's $9.5 billion tourism industry - both built around the Sound!!";
    NSString *fact5 = @"Americans make more than 200 million tons of garbage each year, enough to fill Busch Stadium from top to bottom twice a day. Next time you’re at a sporting event or tailgate, host a trash-free tailgate using only recyclable materials!!! ";
    NSString *fact6 = @"You really need to find a better use of your time.";
    
    self.facts = [[NSMutableArray alloc] initWithObjects: fact1, fact2, fact3, fact4, fact5, nil];
    
    if(self.userScore > 1000)
    {
        self.factsView.text = fact6;
    }
    else if (self.userScore > 200)
    {
        self.factsView.text = fact1;
    }
    else if(self.userScore > 150)
    {
        self.factsView.text = fact2;
    }
    else if(self.userScore > 100)
    {
        self.factsView.text = fact3;
    }
    else if(self.userScore > 50)
    {
        self.factsView.text = fact4;
    }
    else if (self.userScore >= 0)
    {
        self.factsView.text = fact5;
    }
}

#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
    ScoreViewController *scoreVC = (ScoreViewController *)segue.destinationViewController;
    scoreVC.highScore = self.highScore;
    scoreVC.userScore = self.userScore;
}


@end
