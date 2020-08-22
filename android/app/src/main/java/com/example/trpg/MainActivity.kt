package com.example.trpg

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley


class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun connect(btn:android.view.View) {
        val field = findViewById<TextView>(R.id.textView)

        val queue = Volley.newRequestQueue(this)
        val url = "http://riisatoro.pythonanywhere.com/api/v1/server/"

// Request a string response from the provided URL.
        val stringRequest = StringRequest(Request.Method.GET, url,
                Response.Listener<String> { response ->
                    // Display the first 500 characters of the response string.
                    field.text = "Response is: ${response.substring(0)}"
                },
                Response.ErrorListener { field.text = "That didn't work!" })

// Add the request to the RequestQueue.
        queue.add(stringRequest)

        field.text = "Hello pussy"
    }
}