using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Controller : MonoBehaviour
{
    public float horizontalSpeed;
    float speedX;
    public float verticalImpulse;
    Rigidbody2D rb;
    bool isGrounded;
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    public void LeftButtonDown()
    {
        speedX = -horizontalSpeed;
    }
    public void RightButtonDown()
    {
        speedX = horizontalSpeed;
    }
    public void Stop()
    {
        speedX = 0;
    }
    public void OnClickJump()
    {
        if (isGrounded) 
            rb.AddForce(new Vector2(0, verticalImpulse), ForceMode2D.Impulse);
    }
    
    void FixedUpdate()
    {
        transform.Translate(speedX, 0, 0);
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "Ground")
            isGrounded = true;
    }
    private void OnCollisionExit2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "Ground")
            isGrounded = false;
    }
}
