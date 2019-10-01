using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class TextScript : MonoBehaviour
{

    public Text counterText;
    static float count;
    static float coefficient;


    public static void SetCoeficient (float f)
    {
        if (f != 0)
            coefficient = f;
        else
            Debug.Log("Вася ты дебил!");
    }

    public static float Coeff
    {
        get { return coefficient; }
        set
        {
            if (value != 0)
                coefficient = value;
            else
                Debug.Log("Вася ты дебил!");
        }
    }
    public static float GetCoeficient()
    {
        return coefficient;
    }
    void Start()
    {
        coefficient = 2;
        counterText.text = "";
        count = 0;
    }
    public static void PlusCount ()
    {
        count+=1/coefficient;
    }

   
    void Update()
    {
        counterText.text = count.ToString();
    }
}
