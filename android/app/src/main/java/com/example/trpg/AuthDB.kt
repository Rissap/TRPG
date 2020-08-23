package com.example.trpg

import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

val DB_NAME = "trpg_db"
val TABLE_NAME = "user_auth"

class DB(context: Context): SQLiteOpenHelper(context, DB_NAME, null, 1) {
    override fun onCreate(p0: SQLiteDatabase?) {
        var query = "CREATE TABLE user_auth IF NOT EXISTS (id integer, username text, email text, password text, token text);"
        p0?.execSQL(query)
    }

    override fun onUpgrade(p0: SQLiteDatabase?, p1: Int, p2: Int) {
        TODO("Not yet implemented")
    }
}



class User {
    var id:Int = -1
    var username: String = ""
    var email: String = ""
    var password: String = ""
    var token: String = ""

    constructor(id:Int, username:String, email:String, password:String, token:String) {
        this.id = id
        this.username = username
        this.email = email
        this.password = password
        this.token = token
    }
}

