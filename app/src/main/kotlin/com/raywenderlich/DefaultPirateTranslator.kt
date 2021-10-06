// src/main/kotlin/com/raywenderlich/DefaultPirateTranslator.kt
package com.raywenderlich

class DefaultPirateTranslator : PirateTranslator {

    // 1
    val replacements = mapOf("Hello" to "Ahoy!", "Yes" to "Aye!", "Yes, Captain!" to "Aye Aye!")
    
    override fun translate(message: String): String {
        var result = message
        // 2
        replacements.forEach { k, v -> result =    result.replace(k, v) }
        return result
    }
}
