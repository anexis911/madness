using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Teleport : MonoBehaviour
{

    GameObject[] units;


    void Start()
    {
        units = GameObject.FindGameObjectsWithTag("Player");
    }


    void Update()
    {
        if ((Time.time >2) && (Time.time <2.3))
        {
            foreach (GameObject unit in units)
                unit.transform.position = new Vector2(unit.transform.position.x, unit.transform.position.y + 1);
           
        }
    }
}
