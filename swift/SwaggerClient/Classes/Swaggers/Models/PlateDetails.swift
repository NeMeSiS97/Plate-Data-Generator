//
// PlateDetails.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


public class PlateDetails: JSONEncodable {
    /** Best plate number for this plate */
    public var plate: String?
    /** Indicates whether the plate matched a regional text pattern */
    public var matchesTemplate: Int32?
    /** The max number of results requested */
    public var requestedTopn: Int32?
    /** Number of milliseconds to process the license plate */
    public var processingTimeMs: Double?
    /** Confidence percentage that the plate number is correct */
    public var confidence: Double?
    /** Specified or detected region (e.g., tx for Texas) */
    public var region: String?
    /** Confidence percentage that the plate region is correct */
    public var regionConfidence: Double?
    /** The X/Y coordinates of the license plate in the image Four coordinates are provided that form a polygon starting from the top-left and moving clockwise ending in the bottom left  */
    public var coordinates: [Coordinate]?
    /** All the top N candidates that could be the correct plate number */
    public var candidates: [PlateCandidate]?
    public var vehicleRegion: RegionOfInterest?
    public var vehicle: VehicleDetails?

    public init() {}

    // MARK: JSONEncodable
    func encodeToJSON() -> AnyObject {
        var nillableDictionary = [String:AnyObject?]()
        nillableDictionary["plate"] = self.plate
        nillableDictionary["matches_template"] = self.matchesTemplate?.encodeToJSON()
        nillableDictionary["requested_topn"] = self.requestedTopn?.encodeToJSON()
        nillableDictionary["processing_time_ms"] = self.processingTimeMs
        nillableDictionary["confidence"] = self.confidence
        nillableDictionary["region"] = self.region
        nillableDictionary["region_confidence"] = self.regionConfidence
        nillableDictionary["coordinates"] = self.coordinates?.encodeToJSON()
        nillableDictionary["candidates"] = self.candidates?.encodeToJSON()
        nillableDictionary["vehicle_region"] = self.vehicleRegion?.encodeToJSON()
        nillableDictionary["vehicle"] = self.vehicle?.encodeToJSON()
        let dictionary: [String:AnyObject] = APIHelper.rejectNil(nillableDictionary) ?? [:]
        return dictionary
    }
}
