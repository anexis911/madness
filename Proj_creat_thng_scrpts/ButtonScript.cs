using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ButtonScript : MonoBehaviour
{
   
    public void OnClickButton ()
    {
        TextScript.PlusCount();
        TextScript.Coeff -= 0.5f;


    }
}
