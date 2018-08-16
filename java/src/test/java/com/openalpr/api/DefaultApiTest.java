/*
 * OpenALPR Cloud API
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 2.0.1
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.openalpr.api;

import com.openalpr.api.invoker.ApiException;
import java.io.File;
import com.openalpr.api.models.InlineResponse200;
import com.openalpr.api.models.InlineResponse400;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Ignore
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    
    /**
     * 
     *
     * Send an image for OpenALPR to analyze and provide metadata back The image is sent as base64 encoded bytes. 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void recognizeBytesTest() throws ApiException {
        String imageBytes = null;
        String secretKey = null;
        String country = null;
        Integer recognizeVehicle = null;
        String state = null;
        Integer returnImage = null;
        Integer topn = null;
        String prewarp = null;
        InlineResponse200 response = api.recognizeBytes(imageBytes, secretKey, country, recognizeVehicle, state, returnImage, topn, prewarp);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * Send an image for OpenALPR to analyze and provide metadata back The image is sent as a file using a form data POST 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void recognizeFileTest() throws ApiException {
        File image = null;
        String secretKey = null;
        String country = null;
        Integer recognizeVehicle = null;
        String state = null;
        Integer returnImage = null;
        Integer topn = null;
        String prewarp = null;
        InlineResponse200 response = api.recognizeFile(image, secretKey, country, recognizeVehicle, state, returnImage, topn, prewarp);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * Send an image for OpenALPR to analyze and provide metadata back The image is sent as a URL.  The OpenALPR service will download the image  and process it 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void recognizeUrlTest() throws ApiException {
        String imageUrl = null;
        String secretKey = null;
        String country = null;
        Integer recognizeVehicle = null;
        String state = null;
        Integer returnImage = null;
        Integer topn = null;
        String prewarp = null;
        InlineResponse200 response = api.recognizeUrl(imageUrl, secretKey, country, recognizeVehicle, state, returnImage, topn, prewarp);

        // TODO: test validations
    }
    
}
