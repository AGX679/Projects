//
//  IOCMath.m
//  IntroToObjCLibrary
//
//  Created by Abraham Avnisan on 1/31/17.
//  Copyright © 2017 Abraham Avnisan. All rights reserved.
//

#import "IOCMath.h"

@implementation IOCMath

// RANDOM
- (int)getRandomIntWithMinOutput:(int)minOutput maxOutput:(int)maxOutput
{
    if (minOutput > maxOutput) {
        NSLog(@"ERROR! minOutput is greater than maxOutput");
        exit(EXIT_FAILURE);
    }
    
    if (minOutput < 0 || maxOutput < 0) {
        NSLog(@"ERROR! min and max must be greater than or equal to 0");
        exit(EXIT_FAILURE);
    }
    
    uint32_t maxOutputAdjusted = maxOutput + 1; // arc4random_uniform returns a number *LESS* than its argument
    uint32_t maxInput = maxOutputAdjusted - minOutput;
    uint32_t randomRaw = arc4random_uniform(maxInput);
    uint32_t randomAdjusted = randomRaw + minOutput;
    return (int)randomAdjusted;
}
- (NSUInteger)getRandomIntegerWithMinOutput:(NSUInteger)minOutput maxOutput:(NSUInteger)maxOutput
{
    if (minOutput > maxOutput) {
        NSLog(@"ERROR! minOutput is greater than maxOutput");
        exit(EXIT_FAILURE);
    }
    
    uint32_t maxOutputAdjusted = (uint32_t)maxOutput + 1; // arc4random_uniform returns a number *LESS* than its argument
    uint32_t maxInput = maxOutputAdjusted - (uint32_t)minOutput;
    uint32_t randomRaw = arc4random_uniform(maxInput);
    uint32_t randomAdjusted = randomRaw + (uint32_t)minOutput;
    return (NSUInteger)randomAdjusted;
}
- (float)getRandomFloatWithMinOutput:(float)minOutput maxOutput:(float)maxOutput
{
    if (minOutput > maxOutput) {
        NSLog(@"ERROR! minOutput is greater than maxOutput");
        exit(EXIT_FAILURE);
    }
    
    if (minOutput < 0 || maxOutput < 0) {
        NSLog(@"ERROR! min and max must be greater than or equal to 0");
        exit(EXIT_FAILURE);
    }
    
    int multiplier = 100000;
    
    int minOutputAdjusted = (int)(minOutput * multiplier);
    int maxOutputAdjusted = (int)(maxOutput * multiplier);
    
    int randomIntRaw = [self getRandomIntWithMinOutput:minOutputAdjusted maxOutput:maxOutputAdjusted];
    float randomFloat = randomIntRaw / (float)multiplier;
    
    return randomFloat;
}
- (float)getRandomFloat
{
    int multiplier = 100000;
    uint32_t randomRaw = arc4random_uniform(multiplier + 1);
    float randomFloat = randomRaw / (float)multiplier;
    return randomFloat;
}

// MAPPING
- (float)getMappedValueWithInput:(float)input
                        minInput:(float)minInput
                        maxInput:(float)maxInput
                       minOutput:(float)minOutput
                       maxOutput:(float)maxOutput
{
    return minOutput + (maxOutput - minOutput) * (input - minInput) / (maxInput - minInput);
}

- (float)getClampedMappedValueWithInput:(float)input
                               minInput:(float)minInput
                               maxInput:(float)maxInput
                              minOutput:(float)minOutput
                              maxOutput:(float)maxOutput
{
    float mappedValue = minOutput + (maxOutput - minOutput) * (input - minInput) / (maxInput - minInput);
    if (mappedValue > maxOutput) mappedValue = maxOutput;
    if (mappedValue < minOutput) mappedValue = minOutput;
    return mappedValue;

}


// CONVERSION
- (float)convertRadiansToDegrees:(float)radians
{
    return (radians * 180.0) / M_PI;
}
- (float)convertDegreesToRadians:(float)degrees
{
    return (degrees * M_PI) / 180.0;
}

@end
