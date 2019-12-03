using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MuiscCont : MonoBehaviour {

	// Use this for initialization
	void Awake () {
		//used for backgrond music track
		GameObject[] objects = GameObject.FindGameObjectsWithTag ("Music");
		if (objects.Length < 1)
			Destroy (this.gameObject);
		DontDestroyOnLoad (this.gameObject);
	}
	

}
