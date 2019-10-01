using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UnitScript : MonoBehaviour
{

    public bool b = false;
    public float delta = 2;


   
    void Start()
    {
        transform.position = new Vector2(transform.position.x, 1);
    }


    private void Update()
    {
        transform.position = new Vector2(transform.position.x+1* Time.deltaTime,transform.position.y);
       



       /* StartCoroutine(Slow());

         }


     }

     IEnumerator Slow ()
     {
         delta = 0.5f;
         yield return new WaitForSeconds(2);
         delta = 2f;
     }
     */


    }
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.tag == "Exit")
        {
            transform.position = (new Vector2(transform.position.x-3,transform.position.y+3));
        }
    }

}
