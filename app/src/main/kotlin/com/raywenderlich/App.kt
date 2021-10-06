//src/main/kotlin/com/raywenderlich/App.kt
package com.raywenderlich

import com.amazonaws.services.lambda.runtime.Context
import com.amazonaws.services.lambda.runtime.RequestHandler

// 1
class App : RequestHandler<HandlerInput, HandlerOutput> {
    // 2
    val translator : PirateTranslator =   DefaultPirateTranslator()

    // 3
    override fun handleRequest(input: HandlerInput?, context: Context?): HandlerOutput {
        input?.let {
            // 4
            return HandlerOutput(it.message, translator.translate(it.message))
        }
        return HandlerOutput("", "");
    }
}    
