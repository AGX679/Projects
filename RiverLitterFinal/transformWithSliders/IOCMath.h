//
//  IOCMath.h
//  IntroToObjCLibrary
//
//  Created by Abraham Avnisan on 1/31/17.
//  Copyright © 2017 Abraham Avnisan. All rights reserved.
//

#import <Foundation/Foundation.h>

/**
 * @Class IOCMath
 * @Discussion  This class provides some math easy to use math utilities
 *              for getting random numbers, mapping a value from one range
 *              onto a different range, and converting between radians and
 *              and degrees.
 */
@interface IOCMath : NSObject

// METHODS RELATED TO RANDOM NUMBERS
// ________________________________________________________________________________________________ //

/**
 * @discussion  a method that produces a random integer between the
 *              two arguments sent to it. The return value is 
 *              inclusive of the range defined by minOutput and 
 *              maxOutput
 *
 * @param minOutput the lowest integer value that the method 
 *        can possibly return
 *
 * @param maxOutput the highest integer value that the method 
 *        can possibly return
 *
 * @return a random int value within the defined range
 *
 * @warning minOutput must be greater than or equal to 0
 */
- (int)getRandomIntWithMinOutput:(int)minOutput maxOutput:(int)maxOutput;

/**
 * @discussion  a method that produces a random integer between the
 *              two arguments sent to it. The return value is
 *              inclusive of the range defined by minOutput and
 *              maxOutput
 *
 * @param minOutput the lowest integer value that the method
 *        can possibly return
 *
 * @param maxOutput the highest integer value that the method
 *        can possibly return
 *
 * @return a random NSUInteger value within the defined range
 *
 * @warning minOutput must be greater than or equal to 0
 */
- (NSUInteger)getRandomIntegerWithMinOutput:(NSUInteger)minOutput maxOutput:(NSUInteger)maxOutput;

/**
 * @discussion  a method that produces a random integer between the
 *              two arguments sent to it. The return value is
 *              inclusive of the range defined by minOutput and
 *              maxOutput
 *
 * @param minOutput the lowest float value that the method
 *        can possibly return
 *
 * @param maxOutput the highest float value that the method
 *        can possibly return
 *
 * @return a random float value within the defined range
 *
 * @warning minOutput must be greater than or equal to 0
 */
- (float)getRandomFloatWithMinOutput:(float)minOutput maxOutput:(float)maxOutput;

/**
 * @discussion  a method that produces a random float value
 *              between the values of 0 and 1
 *
 * @return a random float value between 0.0 and 1.0
 */
- (float)getRandomFloat;

// METHODS RELATED TO MAPPING VALUES
// ________________________________________________________________________________________________ //

- (float)getMappedValueWithInput:(float)input
                        minInput:(float)minInput
                        maxInput:(float)maxInput
                       minOutput:(float)minOutput
                       maxOutput:(float)maxOutput;

- (float)getClampedMappedValueWithInput:(float)input
                               minInput:(float)minInput
                               maxInput:(float)maxInput
                              minOutput:(float)minOutput
                              maxOutput:(float)maxOutput;

// CONVERSION BETWEEN RADIANS AND DEGREES
// ________________________________________________________________________________________________ //

- (float)convertRadiansToDegrees:(float)radians;
- (float)convertDegreesToRadians:(float)degrees;

@end
