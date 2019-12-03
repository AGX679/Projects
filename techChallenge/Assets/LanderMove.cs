using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LanderMove : MonoBehaviour
{
    public float speed = -5f;
    public float sec =5f;
    public float timeStamp = 0.0f;

    void Start()
    {
        timeStamp = Time.realtimeSinceStartup + sec;

    }

    void Update()
    {
        if (Time.realtimeSinceStartup > timeStamp)
        transform.Translate(0,-speed * Time.deltaTime, 0);
    }


}