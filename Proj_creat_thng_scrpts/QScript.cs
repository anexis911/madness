using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QScript : MonoBehaviour
{
    private void OnMouseDown()
    {
        gameObject.GetComponent<SpriteRenderer>().color = Color.red;
    }
}
